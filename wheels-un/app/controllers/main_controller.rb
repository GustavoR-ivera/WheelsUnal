class MainController < ApplicationController
  include CurrentTripBucket
  before_action :set_bucket, only: %i[ home ]
  before_action :authenticate_user!

  def statistics
      @user = current_user
      @history = @user.trips
  end

  def home
    if current_user
      @user = current_user
      @available_trips = Trip.where("status = 0")
    else
      redirect_to new_user_session_path
    end
  end

end
