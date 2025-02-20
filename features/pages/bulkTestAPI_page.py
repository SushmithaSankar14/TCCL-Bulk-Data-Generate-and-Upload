import random
import string
import requests
import logging
from features.pages.bulkdatagenerate_page import DataGenerator


class APIrsponseCheck:
    def __init__(self):
        # self.driver = driver

        super().__init__()
    # context.logger = logging.getLogger()
    # Configure logging
    logging.basicConfig(level=logging.INFO,
                        format="%(asctime)s - %(levelname)s - %(message)s")

    def verify_serial_number_with_pagination(transaction_id, stb_numbers, page_size=10):
        """
        Verify if the STB numbers exist using API pagination and return the verified STB numbers.

        :param transaction_id: Transaction ID for the API request.
        :param stb_numbers: List of generated STB numbers to verify.
        :param page_size: Number of records per page in API response.
        :return: List of verified STB numbers.
        """
        # API endpoint and token
        endpoint_url = "https://stage-tcclapi.theproindia.com/stb/getStbCreateOrTransferLogs"
        # Replace <your_token_here> with the actual token.
        bearer_token = "Bearer eyJhbGciOiJSUzI1NiIsImtpZCI6IkRDNkExODg1NjE5RTYxREQyRkZEQjZFQTkwMTE1QUM2IiwidHlwIjoiYXQrand0In0.eyJpc3MiOiJodHRwOi8vc3RhZ2UtdGNjbC1pZGVudGl0eWFwaS50aGVwcm9pbmRpYS5jb20iLCJuYmYiOjE3MzYxNDEwNDYsImlhdCI6MTczNjE0MTA0NiwiZXhwIjoxNzM2NzQ1ODQ2LCJzY29wZSI6WyJJZGVudGl0eVNlcnZlckFwaSIsIm9wZW5pZCIsInByb2ZpbGUiLCJ0Y2NsQ2xpZW50U2NvcGUiLCJvZmZsaW5lX2FjY2VzcyJdLCJhbXIiOlsicHdkIl0sImNsaWVudF9pZCI6IndlYiIsInN1YiI6ImQxM2VlNjkzLTJjM2ItNDcxNi04YzZiLTczMzRiNzg4ODMyNiIsImF1dGhfdGltZSI6MTczNjE0MTA0NiwiaWRwIjoibG9jYWwiLCJuYW1lIjoiQUQxNzMwNzkwNTM2MDkyIiwicm9sZSI6IkFkbWluIiwibW9uZ29JZCI6IjY3MjljNDg4M2Q4MmZjN2JmNmZjMzRjNCIsInVzZXJJZCI6IkFEMTczMDc5MDUzNjA5MiIsInVzZXJUeXBlIjoiQWRtaW4iLCJ1c2VyTmFtZSI6IlZpbWFsYSIsInJlZ2lvbnMiOiI2NmI0OWQ1NmZjMjIwNDY2Yjg1ZTdlNDEiLCJqdGkiOiI2MTJENTM1NTc0MTcxRDFDMDcyMzE0QkRGMzhFNkI2QyJ9.K5Q_KBQBkiQC0FvtyhQwx9ID7pydmjGkaw2x_gZqPsiAfynrd2_v-S7gSyyQ82m1zc-ZNWXXjYZZVjab8WspP9PZU4sUS4v5lXlh1IMgfU8oQadTcagd5SHeGFDoWIbuq1JGZ58hYoIWZ_bTg8_h-CbOJY9F1DZ0HfewXbfMPeR5boxMtqk1J2ahxg1W2APLEwRPIjR6pDa--LmGTB0LITiWrh6OMBJUy7LQqw3eWEenIB6svfSTzCMRLHD7OWZ0-vH3TGSz9_W3WWTuh-KcbKazb6BAiyKtMXM2OrCij_mgYWtE5L6bXlM1f3G93tSORyQSww_3EjrBvB-QD1BMyg"

        # Headers
        headers = {
            "Authorization": bearer_token,
            "Content-Type": "application/json"
        }

        page_number = 1
        verified_stb_numbers = []

        while True:
            # Prepare payload for current page
            payload = {
                "transactionId": transaction_id,
                "actionType": "Create",
                "pageNumber": page_number,
                "pageSize": page_size
            }

            try:
                # Send POST request
                response = requests.post(
                    endpoint_url, json=payload, headers=headers)
                response.raise_for_status()

                # Parse response
                data = response.json()
                logs = data.get("logs", [])

                if not logs:
                    logging.info(f"No more logs found on page {page_number}.")
                    break

                # Extract serial numbers from logs
                api_serial_numbers = {log.get("serialNumber") for log in logs}

                # Check for matches
                for stb_number in stb_numbers:
                    if stb_number in api_serial_numbers:
                        logging.info(f"STB number '{stb_number}' verified.")
                        verified_stb_numbers.append(stb_number)

                # Increment page number for next iteration
                page_number += 1

            except requests.exceptions.RequestException as e:
                logging.error(f"Error occurred during API request: {e}")
                break

        # Filter out STB numbers that were found in the API logs
        filtered_stb_numbers = [
            stb for stb in stb_numbers if stb not in verified_stb_numbers]

        # Check for mismatched numbers
        mismatched_stb_numbers = [
            stb for stb in stb_numbers if stb not in verified_stb_numbers]
        if mismatched_stb_numbers:
            logging.warning(f"STB numbers not found in logs: {mismatched_stb_numbers}")

        logging.info(f"Filtered STB numbers (after removing found ones): {filtered_stb_numbers}")

        return filtered_stb_numbers
