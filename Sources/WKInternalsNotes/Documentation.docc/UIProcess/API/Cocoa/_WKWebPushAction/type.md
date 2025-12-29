# ``WKInternalsNotes/_WKWebPushAction/type``

Web Push アクションの種別文字列を返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly) NSString *type;
```

## Default Value
`nil`（生成時に設定される）。

## Discussion
インスタンス生成時に設定される読み取り専用プロパティ。辞書から生成する場合は `dictionary` の type をそのまま設定し、通知応答から生成する場合は `_WKWebPushActionTypeNotificationClick` または `_WKWebPushActionTypeNotificationClose` を設定する。

## References
- [`_WKWebPushAction.h#L30`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebPushAction.h#L30)
- [`_WKWebPushAction.mm#L44`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebPushAction.mm#L44)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-29 |
