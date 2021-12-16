const AWS = require('aws-sdk');

const functionName = process.env.AWS_LAMBDA_FUNCTION_NAME;
const encrypted = process.env['databaseUser'];
let decrypted;
exports.handler = async (event) => {
    if (!decrypted) {
        // Decrypt code should run once and variables stored outside of the
        // function handler so that these are decrypted once per container
        const kms = new AWS.KMS();
        try {
            const req = {
                CiphertextBlob: Buffer.from(encrypted, 'base64'),
                EncryptionContext: { LambdaFunctionName: functionName },
            };
            const data = await kms.decrypt(req).promise();
            decrypted = data.Plaintext.toString('ascii');
              console.log('Decrypt message:', decrypted);

        } catch (err) {
            console.log('Decrypt error:', err);
            throw err;
        }
        };

     let responseBody = {message: decrypted};
     let response = {statusCode: '200',
           body: responseBody
      };
      console.log("response: " + JSON.stringify(response))
      return response;
  };
 