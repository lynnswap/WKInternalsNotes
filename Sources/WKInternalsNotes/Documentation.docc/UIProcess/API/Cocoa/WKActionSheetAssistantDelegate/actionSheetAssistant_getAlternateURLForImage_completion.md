# ``WKInternalsNotes/WKActionSheetAssistantDelegate/actionSheetAssistant(_:getAlternateURLForImage:completion:)``

画像の代替 URL を取得する。

## Objective-C Declaration
```objective-c
- (void)actionSheetAssistant:(WKActionSheetAssistant *)assistant getAlternateURLForImage:(UIImage *)image completion:(void (^)(NSURL *alternateURL, NSDictionary *userInfo))completion;
```

## Discussion
`UIDelegate` が `_webView:getAlternateURLFromImage:completionHandler:` に応答する場合はその結果を `completion` に渡す。未実装の場合は `completion(nil, nil)` を呼ぶ。

## References
- [`WKActionSheetAssistant.h#L59`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKActionSheetAssistant.h#L59)
- [`WKContentViewInteraction.mm#L10155`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L10155)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
