# ``WKInternalsNotes/_WKInspector/connect()``

インスペクタフロントエンドの接続を開始する。

## Objective-C Declaration
```objective-c
- (void)connect;
```

## Discussion
検査対象ページが存在し、Developer Extras が有効で、まだ Show メッセージを送っていない場合にフロントエンドページを作成して WebInspector::Show を送信する。条件を満たさない場合は何もしない。

## References
- [`_WKInspector.h#L52`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKInspector.h#L52)
- [`_WKInspector.mm#L140`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKInspector.mm#L140)
- [`WebInspectorUIProxy.cpp`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Inspector/WebInspectorUIProxy.cpp)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
