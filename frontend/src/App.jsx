import { useState } from "react";
import axios from "axios";

import Sidebar from "./components/Sidebar";
import Header from "./components/Header";
import ChatWindow from "./components/ChatWindow";
import ChatInput from "./components/ChatInput";
import TypingIndicator from "./components/TypingIndicator";

import "./App.css";

function App() {
  const [messages, setMessages] =
    useState([]);

  const [loading, setLoading] =
    useState(false);

  const [chats, setChats] =
    useState(["Welcome Chat"]);

  const sendMessage = async (
    text
  ) => {
    const userMessage = {
      role: "user",
      content: text,
    };

    setMessages((prev) => [
      ...prev,
      userMessage,
    ]);

    setLoading(true);

    try {
      const response =
        await axios.get(
          "http://127.0.0.1:8000/agent",
          {
            params: {
              question: text,
              session_id:
                "prince-session",
            },
          }
        );

      const aiMessage = {
        role: "assistant",
        content:
          response.data.answer,
      };

      setMessages((prev) => [
        ...prev,
        aiMessage,
      ]);
    } catch (err) {
      setMessages((prev) => [
        ...prev,
        {
          role: "assistant",
          content:
            "Unable to contact Jarvis.",
        },
      ]);
    }

    setLoading(false);
  };

  const newChat = () => {
    setMessages([]);
  };

  return (
    <div className="layout">
      <Sidebar
        chats={chats}
        onNewChat={newChat}
      />

      <div className="main">
        <Header />

        <ChatWindow
          messages={messages}
        />

        {loading && (
          <TypingIndicator />
        )}

        <ChatInput
          onSend={sendMessage}
          loading={loading}
        />
      </div>
    </div>
  );
}

export default App;