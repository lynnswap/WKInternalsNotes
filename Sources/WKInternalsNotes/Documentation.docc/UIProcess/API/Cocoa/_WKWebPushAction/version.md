# ``WKInternalsNotes/_WKWebPushAction/version``

Web Push アクションのバージョン番号を返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly) NSNumber *version;
```

## Default Value
`nil`（辞書から生成した場合に設定される）。

## Discussion
内部で読み書き可能なプロパティで、`webPushActionWithDictionary:` が `dictionary` から取得した `NSNumber` を設定する。通知応答から生成する経路では設定されない。

## References
- [`_WKWebPushAction.h#L45`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebPushAction.h#L45)
- [`_WKWebPushAction.mm#L42`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebPushAction.mm#L42)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-29 |
