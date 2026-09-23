class APIConfig:

    """Manages configuration settings for external AI API endpoints."""

    def __init__(

        self,

        model: str,

        base_url: str,

        timeout: int = 30,

        max_retries: int = 3,

    ):

        # Setting instance attributes

        self.model = model

        self.base_url = base_url

        self.timeout = timeout

        self.max_retries = max_retries

    def get_summary(self) -> str:

        return (

            f"Model: {self.model} | Base URL: {self.base_url} | "


        )


# Object 1: Created using Positional Arguments & Default Values

config_1 = APIConfig("gpt-4o", "https://api.openai.com/v1")

# Object 2: Created using Keyword / Named Arguments & Overridden Defaults

config_2 = APIConfig(

    model="claude-3-5-sonnet",

    base_url="https://api.anthropic.com/v1",

    timeout=60,

    max_retries=5,

)

# Object 3: Created using Mixed Positional and Keyword Arguments

config_3 = APIConfig(

    "gemini-1.5-pro",

    "https://generativelanguage.googleapis.com/v1beta",

    timeout=45,

)

# Output test verification

if __name__ == "__main__":

    print("API Configuration System Initialized:\n")

    print(f"Config 1: {config_1.get_summary()}")

    print(f"Config 2: {config_2.get_summary()}")

    print(f"Config 3: {config_3.get_summary()}")

