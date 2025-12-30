# ``WKInternalsNotes/_WKElementAction/_elementActionWithType(_:info:assistant:disabled:)``

要素情報に応じたタイトルを付与してアクションを作成する。

## Objective-C Declaration
```objective-c
+ (instancetype)_elementActionWithType:(_WKElementActionType)type info:(_WKActivatedElementInfo *)info assistant:(WKActionSheetAssistant *)assistant disabled:(BOOL)disabled;
```

## Discussion
`Copy` かつリンクで画像でない場合は `"Copy Link"` をカスタムタイトルとして設定し、`_elementActionWithType:customTitle:assistant:disabled:` に委譲する。

## References
- [`_WKElementActionInternal.h#L37`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKElementActionInternal.h#L37)
- [`_WKElementAction.mm#L244`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKElementAction.mm#L244)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
