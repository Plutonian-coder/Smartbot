# test/test_models.py

import unittest
import os
from src.config import NLP_MODEL_PATH
from model.nlp_controller import get_bot_response
from model.train_nlp_model import train_model

class TestNLPModel(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """
        Train a fresh model before running tests to ensure consistency.
        This ensures tests don't fail due to a missing or stale model file.
        """
        print("Training a temporary model for testing...")
        # We run the training script to ensure the model file exists
        train_model()

    def test_model_file_exists(self):
        """
        Tests if the model file is created after training.
        """
        self.assertTrue(os.path.exists(NLP_MODEL_PATH), "NLP model file should exist after training.")

    def test_get_bot_response(self):
        """
        Tests the get_bot_response function with a sample query.
        """
        # This query is based on the sample data in faq_data.csv
        query = "how do I pay my fees?"
        response = get_bot_response(query)

        # We expect a response related to school fees
        self.assertIn("student portal", response.lower(), "Response should contain information about payment.")

    def test_unknown_query(self):
        """
        Tests how the model handles a query it likely doesn't know.
        Note: The simple model might still match this to a known intent.
        A more robust test would mock the model's prediction.
        """
        query = "what is the meaning of life?"
        response = get_bot_response(query)

        # This tests the fallback response
        self.assertIn("i'm not sure", response.lower(), "Should provide a fallback for unknown queries.")


if __name__ == '__main__':
    unittest.main()
