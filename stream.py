{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "from twython import TwythonStreamer\n",
    "\n",
    "from auth import (\n",
    "    consumer_key,\n",
    "    consumer_secret,\n",
    "    access_token,\n",
    "    access_token_secret\n",
    ")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "class MyStreamer(TwythonStreamer):\n",
    "    def on_success(self, data):\n",
    "        if 'text' in data:\n",
    "            username = data['user']['screen_name']\n",
    "            tweet = data['text']\n",
    "            print(\"@{}: {}\".format(username, tweet))\n",
    "            \n",
    "stream = MyStreamer(\n",
    "    consumer_key,\n",
    "    consumer_secret,\n",
    "    access_token,\n",
    "    access_token_secret\n",
    ")\n",
    "stream.statuses.filter(track='raspberry pi')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
