const pipeline = require("util").promisify(require("stream").pipeline);
const { Readable } = require('stream');

exports.handler = awslambda.streamifyResponse(async (event, responseStream, _context) => {
  // As an example, convert event to a readable stream.
  const requestStream = Readable.from(Buffer.from(JSON.stringify('Hello from Lambda!')));

  await pipeline(requestStream, responseStream);
});
