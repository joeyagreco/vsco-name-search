from service.VSCOService import VSCOService

if __name__ == '__main__':
    vsco_service = VSCOService()
    vsco_service.save_unused_usernames(min_length=5, max_length=5)
