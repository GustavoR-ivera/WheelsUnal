class MainController < ApplicationController
  before_action :authenticate_user!

  def home
    if current_user
      @user = current_user
    else
      redirect_to new_user_session_path
    end
  end
end
