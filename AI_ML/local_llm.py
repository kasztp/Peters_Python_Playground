"""
Local LLM Interaction Module

This module provides utility functions to interact with locally hosted language models via LM Studio server.
It supports various operations including listing available models, generating text completions, chat completions,
and creating embeddings from text input.

Dependencies:
    - requests: For making HTTP requests to the LM Studio server
    - json: For parsing JSON responses

Configuration:
    - BASE_URL: Endpoint URL for the LM Studio server (default: http://localhost:1234/v1)
    - MODEL_NAME: Name of the model to use for inference (default: deepseek-r1-distill-llama-8b)
"""
import json
import logging
from typing import Any, Dict, List, Optional, Union

import requests

# Configuration for local LM Studio server
BASE_URL = "http://localhost:1234/v1"
MODEL_NAME = "deepseek-r1-distill-llama-8b"  # Specify the model name loaded in LM Studio


class LocalLLMClient:
    """Client for interacting with locally hosted language models via LM Studio server."""

    def __init__(
            self,
            base_url: str = "http://localhost:1234/v1",
            model_name: str = "deepseek-r1-distill-llama-8b"
        ):
        """
        Initialize the LocalLLM client.

        Args:
            base_url: Base URL for the LM Studio server
            model_name: Name of the model to use for inference
        """
        self.base_url = base_url
        self.model_name = model_name
        self.logger = logging.getLogger(__name__)

    def list_models(self) -> Optional[Dict[str, Any]]:
        """
        List available models in LM Studio.

        Returns:
            Dictionary containing model information if successful, None otherwise
        """
        try:
            response = requests.get(f"{self.base_url}/models")
            response.raise_for_status()
            models = response.json()

            self.logger.info("Available models:")
            for model in models.get("data", []):
                self.logger.info(f"- {model.get('id')}")

            return models
        except requests.exceptions.RequestException as e:
            self.logger.error(f"Error listing models: {e}")
            return None

    def chat_completion(
        self, 
        messages: List[Dict[str, str]], 
        temperature: float = 0.7, 
        max_tokens: int = 1000
    ) -> Optional[Dict[str, Any]]:
        """
        Generate chat completions using the model.

        Args:
            messages: List of message dictionaries with 'role' and 'content' keys
            temperature: Sampling temperature (0.0 to 1.0)
            max_tokens: Maximum number of tokens to generate

        Returns:
            Dictionary containing the completion result if successful, None otherwise
        """
        data = {
            "model": self.model_name,
            "messages": messages,
            "temperature": temperature,
            "max_tokens": max_tokens
        }

        try:
            response = requests.post(f"{self.base_url}/chat/completions", json=data)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            self.logger.error(f"Error in chat completion: {e}")
            return None

    def text_completion(
        self, 
        prompt: str, 
        temperature: float = 0.7, 
        max_tokens: int = 1000
    ) -> Optional[Dict[str, Any]]:
        """
        Generate text completions using the model.

        Args:
            prompt: Text prompt for completion
            temperature: Sampling temperature (0.0 to 1.0)
            max_tokens: Maximum number of tokens to generate

        Returns:
            Dictionary containing the completion result if successful, None otherwise
        """
        data = {
            "model": self.model_name,
            "prompt": prompt,
            "temperature": temperature,
            "max_tokens": max_tokens
        }

        try:
            response = requests.post(f"{self.base_url}/completions", json=data)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            self.logger.error(f"Error in text completion: {e}")
            return None

    def create_embeddings(self, input_text: Union[str, List[str]]) -> Optional[Dict[str, Any]]:
        """
        Create embeddings from text.

        Args:
            input_text: String or list of strings to create embeddings for

        Returns:
            Dictionary containing the embedding results if successful, None otherwise
        """
        data = {
            "model": self.model_name,
            "input": input_text
        }

        try:
            response = requests.post(f"{self.base_url}/embeddings", json=data)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            self.logger.error(f"Error creating embeddings: {e}")
            return None


def main():
    # Configure logging
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )

    # Initialize the client
    llm_client = LocalLLMClient()

    # List available models
    models = llm_client.list_models()

    # Example chat completion
    chat_messages = [
        {
            "role": "system",
            "content": "You are a helpful AI assistant."
        },
        {
            "role": "user",
            "content": "Explain the advantages of using local LLMs over cloud-based ones."
        }
    ]

    print("\nGenerating chat completion...")
    chat_result = llm_client.chat_completion(chat_messages)
    if chat_result:
        print("\nChat Completion Result:")
        response_content = chat_result["choices"][0]["message"]["content"]
        print(response_content)

    # Example text completion
    prompt = "Local language models are beneficial because"
    print("\nGenerating text completion...")
    completion_result = llm_client.text_completion(prompt)
    if completion_result:
        print("\nText Completion Result:")
        print(completion_result["choices"][0]["text"])

    # Example embeddings (Note: Not all models support embeddings)
    try:
        print("\nGenerating embeddings...")
        embedding_result = llm_client.create_embeddings("Local language models")
        if embedding_result:
            print("\nEmbedding generated successfully.")
            # Print the first few dimensions of the embedding vector
            vector = embedding_result["data"][0]["embedding"]
            print(f"Embedding dimensions: {len(vector)}")
            print(f"First few values: {vector[:5]}...")
    except Exception as e:
        print(f"\nEmbedding generation might not be supported: {e}")


if __name__ == "__main__":
    main()
