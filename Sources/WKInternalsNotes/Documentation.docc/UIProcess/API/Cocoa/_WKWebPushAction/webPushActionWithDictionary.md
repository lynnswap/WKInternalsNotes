# ``WKInternalsNotes/_WKWebPushAction/webPushActionWithDictionary(_:)``

辞書の内容を検証し、`_WKWebPushAction` を生成して返す。

## Objective-C Declaration
```objective-c
+ (_WKWebPushAction *)webPushActionWithDictionary:(NSDictionary *)dictionary;
```

## Discussion
`dictionary` から `version`/`pushPartition`/`type` を取り出し、型が期待通りでなければ `nil` を返す。`pushPartition` は 32 文字の文字列を想定し、UUID に変換できない場合も `nil` を返す。生成したインスタンスに `version`、`webClipIdentifier`、`type` を設定して返す。

## References
- [`_WKWebPushAction.mm#L72`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebPushAction.mm#L72)
- [`_WKWebPushAction.h#L42`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebPushAction.h#L42)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-29 |
