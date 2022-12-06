"""bigwig URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from user.api import UserRegistrationView,LogoutView,UserListView,UserLoginViewFirebaseTokenReplace
from user.api import UserVerifyView,ResendOtpView,UserLoginView,CreateUserView,ResetPasswordView,ResetPasswordView2
from django.conf.urls.i18n import i18n_patterns
from rest_framework import routers
from polls.api2 import PollList, PollDetail, ChoiceList, CreateVote, PollViewSet,VoteViewSet
from feedback.api import FeedBackView
from events.api import EventView,EventLikeView


#token
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

# import project

from projects.api import ProjectView,ProjectTaskView,ProjectInviteView

# import stories

from stories.api import StoriesView,StoriesCommentView,StoriesLikeView,ItemView

## import groupchat

from groupchat.api import GroupView,GroupChatView,GroupListView,MessageView

# import advertisement

from advertisement.api import AdvertismentCategoryView,AdvertisementSubCategoryView,AdvertisementView



#import events
# from events.api import eventdoubleview


# vote validate

from polls.api import votevalidateview


#api import
from location.api import area_view,ward_view,areab
from dashboard.api import VideoView,FeedCommentView,FeedView,FeedCommentView,FeedlikeView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)



router = routers.DefaultRouter()
# router = routers.SimpleRouter()



# events


router.register(r'events',EventView)
router.register(r'eventpoll',EventLikeView)


# router.register(r'eventdouble',eventdoubleview, 'eventdouble')



# feed url

router.register(r'feed',FeedView)
router.register(r'feedcomment',FeedCommentView)
router.register(r'feedlike',FeedlikeView)


#api url 

router.register(r'area',area_view)
router.register(r'ward',ward_view)
router.register(r'video',VideoView)
router.register(r'areab',areab,basename="areab")
router.register(r'votedetails',VoteViewSet)


# polls
router.register(r'pollsresult', PollViewSet)
router.register(r'pollsdetail',PollDetail)
router.register(r'pollslist',PollList)


#vote validate


#feedback
router.register(r'feedback',FeedBackView)



#projects

router.register(r'projects',ProjectView)
router.register(r'projectask',ProjectTaskView)
router.register(r'projectinvite',ProjectInviteView)




#stories view

router.register(r'stories',StoriesView)
router.register(r'storiescomment',StoriesCommentView)
router.register(r'storieslike',StoriesLikeView)
router.register(r'item',ItemView)

#group Chat

router.register(r'group',GroupView)
router.register(r'groupchat',GroupChatView)
router.register(r'grouplist',GroupListView)
router.register(r'message',MessageView)






# advertisement 

router.register(r'category',AdvertismentCategoryView)
router.register(r'subcategory',AdvertisementSubCategoryView)
router.register(r'ads',AdvertisementView)








# user list

router.register(r'userlist',UserListView)


# witable

from writenest.api import TeslaModelListCreateAPIView,CountryNameListCreateAPIView

router.register(r'write1',TeslaModelListCreateAPIView)

router.register(r'write2',CountryNameListCreateAPIView)





from groupchat.api import RegisterFilterAPIView

router.register(r'uuid',RegisterFilterAPIView,basename="uuid")





from broadcast.views import send_noti






urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/register',UserRegistrationView.as_view()),
    path('api/register/new',CreateUserView.as_view()),
    path('api/login', UserLoginView.as_view()),
    path('api/logout/', LogoutView.as_view(), name='auth_logout'),
    # path('api/v1/area/try', areab.as_view()),
    path('api/otp/verify',UserVerifyView.as_view()),
    path('api/otp/resend',ResendOtpView.as_view()),
    path('api/resetpassword',ResetPasswordView2.as_view()),

    path('api/firebaselogin',UserLoginViewFirebaseTokenReplace.as_view()),



    path('api/v1/',include(router.urls)),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),

    path('api/vote',votevalidateview.as_view()),
    path("api/v1/polls/<int:pk>/choices/", ChoiceList.as_view(), name="choice_list"),
    path("api/v1/polls/<int:pk>/choices/<int:choice_pk>/vote",
         CreateVote.as_view(), name="create_vote"),

    #token
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # path('api/uuid',RegisterFilterAPIView.as_view())
    # path("eventdouble/",eventdoubleview.as_view()),

    path('noti/', send_noti, name='send_noti'),



]



    # urlpatterns += i18n_patterns(
    #     path('en/admin/', include(admin.site.urls)),
    # )
