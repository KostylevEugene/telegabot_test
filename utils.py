from clarifai_grpc.channel.clarifai_channel import ClarifaiChannel
from clarifai_grpc.grpc.api import service_pb2, resources_pb2, service_pb2_grpc
from clarifai_grpc.grpc.api.status import status_pb2, status_code_pb2
from pprint import PrettyPrinter
from random import randint
from telegram import ReplyKeyboardMarkup, KeyboardButton
import settings

def play_random_numb(user_numb):
    bot_num = randint(user_numb - 10, user_numb + 10)
    if user_numb > bot_num:
        message = f'Your number is {user_numb}, my number is {bot_num}. You win!'
    elif user_numb == bot_num:
        message = f'Your number is {user_numb}, my number is {bot_num}. Draw!'
    else:
        message = f'Your number is {user_numb}, my number is {bot_num}. You lose!'
    return message


def main_keybord():
    return ReplyKeyboardMarkup([['Send me cat', KeyboardButton('Send my coordinates', request_location=True),
                                 "Fill in the form"]
                                ])


def is_cat(file_name):
    # This is how you authenticate.
    channel = ClarifaiChannel.get_grpc_channel()
    stub = service_pb2_grpc.V2Stub(channel)
    metadata = (('authorization', settings.CLARIFAI_API_KEY),)

    with open(file_name, "rb") as f:
        file_bytes = f.read()

    request = service_pb2.PostModelOutputsRequest(
        # This is the model ID of a publicly available General model. You may use any other public or custom model ID.
        model_id='aaa03c23b3724a16a56b629203edc62c',
        inputs=[
            resources_pb2.Input(data=resources_pb2.Data(image=resources_pb2.Image(base64=file_bytes)))
        ])
    response = stub.PostModelOutputs(request, metadata=metadata)

    # post_model_outputs_response = stub.PostModelOutputs(
    #     service_pb2.PostModelOutputsRequest(
    #         model_id="aaa03c23b3724a16a56b629203edc62c",
    #         version_id="aa9ca48295b37401f8af92ad1af0d91d",
    #         inputs=[
    #             resources_pb2.Input(
    #                 data=resources_pb2.Data(
    #                     image=resources_pb2.Image(
    #                         base64=file_bytes
    #                     )
    #                 )
    #             )
    #         ]
    #     ),
    #     metadata=metadata
    # )
    # print(status_code_pb2.SUCCESS)
    # print(post_model_outputs_response.status.code)
    # if post_model_outputs_response.status.code != status_code_pb2.SUCCESS:
    #     raise Exception("Post model outputs failed, status: " + post_model_outputs_response.status.description)

    # Since we have one input, one output will exist here.
    # output = post_model_outputs_response.outputs[0]

    print("Predicted concepts:")
    for concept in response.outputs[0].data.concepts:
        print("%s %.2f" % (concept.name, concept.value))


#if __name__ == '__main__':
    # print(is_cat('images/cat1.jpg'))
    # pp = PrettyPrinter(indent=2)
    # pp.pprint(is_cat("images/not_cat.jpg"))