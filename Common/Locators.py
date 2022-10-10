class Locators():

    main_logo = "//img[contains(@class,'logo')]"
    topbar_button_signin = "//a[@class='login'][contains(text(),'Sign in')]"
    topbar_button_signout = "//a[@class='logout'][contains(text(),'Sign out')]"

    signin_email = "//input[@id='email']"
    signin_password = "//input[@id='passwd']"
    signin_button = "//button[@id='SubmitLogin']"

    span_my_account = "//span[contains(text(),'My account')]"
    account_order_history = "//ul/li/a/span[contains(text(),'Order history and details')]"
    account_credit_slips = "//ul/li/a/span[contains(text(),'My credit slips')]"
    account_addresses = "//ul/li/a/span[contains(text(),'My addresses')]"
    account_personal_information = "//ul/li/a/span[contains(text(),'My personal information')]"
    account_wishlists = "//ul/li/a/span[contains(text(),'My wishlists')]"
    account_customer_account = "//a[@title='View my customer account']"

    #
    # article_title = "//div[@class='article-page']/div[@class='banner']/div[@class='container']/h1"
    # article_content = "//div[contains(@class, 'article-content')]//p"
    #
    # global_feed_article_preview_title = "//app-article-list//a[@class='preview-link']//h1"
    # global_feed_article_preview_about = "//app-article-list//a[@class='preview-link']//p"
    #
    # profile_username = "//div[@class='profile-page']//h4"