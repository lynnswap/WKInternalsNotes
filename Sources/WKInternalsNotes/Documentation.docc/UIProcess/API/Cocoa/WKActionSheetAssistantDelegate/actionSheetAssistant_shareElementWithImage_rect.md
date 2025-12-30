# ``WKInternalsNotes/WKActionSheetAssistantDelegate/actionSheetAssistant(_:shareElementWithImage:rect:)``

画像を共有シートで共有する。

## Objective-C Declaration
```objective-c
- (void)actionSheetAssistant:(WKActionSheetAssistant *)assistant shareElementWithImage:(UIImage *)image rect:(CGRect)boundingRect;
```

## Discussion
`ShareDataWithParsedURL` に PNG 変換した画像データと既定ファイル名（"Shared Image".png）を詰め、`boundingRect` を `webView` 座標へ変換して共有シートを表示する。

## References
- [`WKActionSheetAssistant.h#L59`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKActionSheetAssistant.h#L59)
- [`WKContentViewInteraction.mm#L10018`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L10018)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
