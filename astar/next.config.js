module.exports = () => {
    const rewrites = () => {
      return [
        {
          source: "/astar/:path*",
          destination: "http://localhost:5000/astar/:path*",
        },
      ];
    };
    return {
      rewrites,
    };
  };
  