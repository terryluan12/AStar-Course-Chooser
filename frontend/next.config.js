module.exports = () => {
    const rewrites = () => {
      return [
        {
          source: "/astar/:path*",
          destination: "http://localhost:3001/astar/:path*",
        },
      ];
    };
    return {
      rewrites,
    };
  };
  