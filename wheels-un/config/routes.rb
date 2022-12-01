Rails.application.routes.draw do

  devise_for :users

  root 'main#home'

  authenticated do
    get '/history', to: 'main#statistics'
    resources :trips
    resources :vehicles
    resources :trip_creators
    resources :line_items
    resources :trip_buckets
  end
  # Define your application routes per the DSL in https://guides.rubyonrails.org/routing.html
end
