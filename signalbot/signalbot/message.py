r:
        try:
            group = message["groupInfo"]["groupId"]
            return group
        except Exception:
            return None

    @classmethod
    def _parse_reaction(self, message: dict) -> str:
        try:
            reaction = message["reaction"]["emoji"]
            return reaction
        except Exception:
            return None

    def __str__(self):
        if self.text is None:
            return ""
        return self.text


class UnknownMessageFormatError(Exception):
    pass
