import json
import time

class DesignAgent:
    def __init__(self):
        self.system_prompt = "You are an expert AI interior designer."
        
    def generate_recommendations(self, room_features, preferences):
        # In a real scenario, this would call an LLM API like OpenAI or Anthropic
        # For demonstration without API keys, we return a structured mock response
        # simulating a chain-of-thought agent.
        print("Agent thinking...")
        time.sleep(2) # Simulate API latency
        
        style_mapping = {
            "wall_color": "A soothing sage green to complement natural light",
            "furniture": ["Mid-century modern sofa", "Glass coffee table", "Ergonomic accent chair"],
            "layout": "Open concept, orienting the seating area towards the main window.",
            "ar_models": [
                {"id": "sofa_001", "name": "Minimalist Sofa", "position": {"x": 0, "y": 0, "z": -2}},
                {"id": "table_002", "name": "Glass Coffee Table", "position": {"x": 0, "y": 0, "z": -1}},
            ]
        }
        
        return {
            "summary": f"Based on the {room_features['room_type']} and your preference for {preferences}, I've designed a balanced layout.",
            "theme": preferences,
            "details": style_mapping,
            "actions": [
                "Order furniture samples",
                "Preview AR models in space",
                "Generate lighting plan"
            ]
        }

    def chat(self, user_message, context):
        time.sleep(1)
        if "sofa" in user_message.lower():
            return "I recommend a modular sofa in a light gray fabric for this space. It provides flexibility and keeps the room feeling open. Would you like to see AR previews of a few options?"
        if "color" in user_message.lower():
            return "Given the natural lighting we detected, warm neutral tones with a bold accent wall (perhaps deep blue) would create a stunning contrast."
        return "That's a great question. Based on the current room analysis, we should focus on maximizing the space perception. What are your thoughts on adding some mirrors?"
