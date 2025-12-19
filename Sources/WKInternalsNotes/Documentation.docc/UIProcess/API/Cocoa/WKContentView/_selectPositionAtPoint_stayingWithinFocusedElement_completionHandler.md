# ``WKInternalsNotes/WKContentView/_selectPositionAtPoint(_:stayingWithinFocusedElement:completionHandler:)``

指定位置の選択を開始する。

## Objective-C Declaration
```objective-c
- (void)_selectPositionAtPoint:(CGPoint)point stayingWithinFocusedElement:(BOOL)stayingWithinFocusedElement completionHandler:(void (^)(void))completionHandler;
```

## Discussion
テキスト選択のコンテキストを更新し、`WebPageProxy::selectPositionAtPoint` を呼んで選択を開始する。完了時にジェスチャ選択中フラグを解除する。

## References
- [`WKContentViewInteraction.h#L763`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.h#L763)
- [`WKContentViewInteraction.mm#L5771`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L5771)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
