import {
  useEffect,
  useRef,
} from "react";

import Message from "./Message";

function ChatWindow({
  messages,
}) {
  const bottomRef =
    useRef(null);

  useEffect(() => {
    bottomRef.current?.scrollIntoView(
      {
        behavior: "smooth",
      }
    );
  }, [messages]);

  return (
    <div className="chat-window">
      {messages.length === 0 ? (
        <div className="welcome">
          <h1>
            Welcome back,
            Prince 👋
          </h1>

          <p>
            Powered by Groq •
            Gemini • OpenAI
          </p>

          <p>
            Memory • Search •
            Tools
          </p>
        </div>
      ) : (
        <>
          {messages.map(
            (message, i) => (
              <Message
                key={i}
                message={message}
              />
            )
          )}

          <div
            ref={bottomRef}
          />
        </>
      )}
    </div>
  );
}

export default ChatWindow;