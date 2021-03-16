# Create image based on nginx and deploy our built React app
FROM nginx:1.17-alpine

#COPY --from=build /app/build /usr/share/nginx/html

#RUN rm /etc/nginx/conf.d/default.conf
COPY nginx.conf /etc/nginx/

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]
