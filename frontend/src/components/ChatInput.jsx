import {
  useState,
} from "react";

import {
  FaPaperPlane,
} from "react-icons/fa";

function ChatInput({
  onSend,
  loading,
}) {
  const [text, setText] =
    useState("");

  const handleSend = () => {
    if (!text.trim()) return;

    onSend(text);
    setText("");
  };

  return (
    <div className="input-container">
      <input
        value={text}
        onChange={(e) =>
          setText(
            e.target.value
          )
        }
        onKeyDown={(e) => {
          if (
            e.key ===
            "Enter"
          ) {
            handleSend();
          }
        }}
        placeholder="Ask Jarvis anything..."
      />

      <button
        disabled={loading}
        onClick={handleSend}
      >
        <FaPaperPlane />
      </button>
    </div>
  );
}

export default ChatInput;