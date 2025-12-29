# ``WKInternalsNotes/WKTextFinderClient/initWithPage(_:view:usePlatformFindUI:)``

ページとビュー、検索UI設定を保持して初期化する。

## Objective-C Declaration
```objective-c
- (instancetype)initWithPage:(std::reference_wrapper<WebKit::WebPageProxy>)page view:(NSView *)view usePlatformFindUI:(BOOL)usePlatformFindUI;
```

## Discussion
`_page` と `_view`、`_usePlatformFindUI` を設定し、ページに `FindMatchesClient`/`FindClient` を登録する。

## References
- [`WKTextFinderClient.h#L40`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/mac/WKTextFinderClient.h#L40)
- [`WKTextFinderClient.mm#L173`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/mac/WKTextFinderClient.mm#L173)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
