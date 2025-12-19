# ``WKInternalsNotes/WKContentView/undoManagerForWebView``

WebView 用の `NSUndoManager` を返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly) NSUndoManager *undoManagerForWebView;
```

## Default Value
編集用キーイベント合成が必要な場合は `WKNSKeyEventSimulatorUndoManager`、それ以外は `WKNSUndoManager` を遅延生成して返す。

## Discussion
フォーカス中の要素がキーイベント合成を要求し、かつ `hasHiddenContentEditable` のときはキーイベントシミュレーション用の Undo マネージャを使用する。

## References
- [`WKContentView.h#L66`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentView.h#L66)
- [`WKContentView.mm#L774`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentView.mm#L774)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
