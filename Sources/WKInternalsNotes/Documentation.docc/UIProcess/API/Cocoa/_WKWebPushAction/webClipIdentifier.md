# ``WKInternalsNotes/_WKWebPushAction/webClipIdentifier``

Web Push 対象の WebClip 識別子を返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly) NSUUID *webClipIdentifier;
```

## Default Value
`nil`（生成時に設定される）。

## Discussion
辞書または通知応答から取り出した `pushPartition` を UUID に変換し、`webClipIdentifier` として保持する。UUID に変換できない場合は生成処理自体が `nil` を返す。

## References
- [`_WKWebPushAction.h#L46`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebPushAction.h#L46)
- [`_WKWebPushAction.mm#L43`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebPushAction.mm#L43)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-29 |
