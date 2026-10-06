export async function onRequest(context) {
  const { env, request } = context;
  const url = new URL(request.url);
  
  const githubAuthUrl = `https://github.com/login/oauth/authorize?client_id=${env.GITHUB_CLIENT_ID}&redirect_uri=${url.origin}/api/callback&scope=repo,user`;
  
  return Response.redirect(githubAuthUrl, 302);
}
