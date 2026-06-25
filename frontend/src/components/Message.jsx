import ReactMarkdown from "react-markdown";

function Message({
  message,
}) {
  return (
    <div
      className={`message ${message.role}`}
    >
      <div className="message-header">
        {message.role ===
        "user"
          ? "Prince"
          : "Jarvis"}
      </div>

      <ReactMarkdown>
        {message.content}
      </ReactMarkdown>
    </div>
  );
}

export default Message;