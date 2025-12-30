# ``WKInternalsNotes/WKActionSheetAssistantDelegate/actionSheetAssistant(_:shareElementWithURL:rect:)``

URL を共有シートで共有する。

## Objective-C Declaration
```objective-c
- (void)actionSheetAssistant:(WKActionSheetAssistant *)assistant shareElementWithURL:(NSURL *)url rect:(CGRect)boundingRect;
```

## Discussion
`ShareDataWithParsedURL` を生成して `url` と `originator` を設定し、`boundingRect` を `webView` 座標へ変換して共有シートを表示する。

## References
- [`WKActionSheetAssistant.h#L59`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKActionSheetAssistant.h#L59)
- [`WKContentViewInteraction.mm#L10010`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L10010)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
