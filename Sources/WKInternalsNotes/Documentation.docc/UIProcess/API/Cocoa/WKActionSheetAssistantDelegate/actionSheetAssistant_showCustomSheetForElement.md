# ``WKInternalsNotes/WKActionSheetAssistantDelegate/actionSheetAssistant(_:showCustomSheetForElement:)``

カスタムシートの表示を委譲する。

## Objective-C Declaration
```objective-c
- (BOOL)actionSheetAssistant:(WKActionSheetAssistant *)assistant showCustomSheetForElement:(_WKActivatedElementInfo *)element;
```

## Discussion
`UIDelegate` が `_webView:showCustomSheetForElement:` に応答する場合に呼び出し、`YES` のときは必要に応じてタッチをキャンセルして `YES` を返す。応答しない場合や `NO` の場合は `NO` を返す。

## References
- [`WKActionSheetAssistant.h#L59`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKActionSheetAssistant.h#L59)
- [`WKContentViewInteraction.mm#L10034`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L10034)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
