# ``WKInternalsNotes/WKFullScreenWindowController/savedConstraints``

フルスクリーン遷移中に退避した Auto Layout 制約を保持する。

## Objective-C Declaration
```objective-c
@property (assign) NSArray *savedConstraints;
```

## Default Value
初期値は `nil`。WebView の差し替え時に退避される。

## Discussion
setter/getter は `_savedConstraints` を保持するだけで、`_saveConstraintsOf:` が `NSAutoresizingMaskLayoutConstraint` を除外して保存する。復帰時に `activateConstraints:` で戻される。

## References
- [`WKFullScreenWindowController.mm#L307`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/mac/WKFullScreenWindowController.mm#L307)
- [`WKFullScreenWindowController.mm#L956`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/mac/WKFullScreenWindowController.mm#L956)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-29 |
