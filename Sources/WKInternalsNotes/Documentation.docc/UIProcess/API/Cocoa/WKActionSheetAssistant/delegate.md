# ``WKInternalsNotes/WKActionSheetAssistant/delegate``

アクションシート操作を委譲するデリゲート。

## Objective-C Declaration
```objective-c
@property (nonatomic, weak) id <WKActionSheetAssistantDelegate> delegate;
```

## Default Value
未設定（`nil`）。

## Discussion
`WeakObjCPtr` で保持し、getter は `getAutoreleased()` を返す。

## References
- [`WKActionSheetAssistant.h#L110`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKActionSheetAssistant.h#L110)
- [`WKActionSheetAssistant.mm#L120`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKActionSheetAssistant.mm#L120)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
