


def apply_sorting(queryset, request, default="-created_at"):
    sort = request.query_params.get("sort")
    if sort == "oldest":
        return queryset.order_by("created_at")
    elif sort == "newest":
        return queryset.order_by("-created_at")
    return queryset.order_by(default)
