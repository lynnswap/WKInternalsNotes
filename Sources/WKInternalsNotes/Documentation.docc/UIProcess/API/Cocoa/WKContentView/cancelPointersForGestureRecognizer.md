# ``WKInternalsNotes/WKContentView/cancelPointersForGestureRecognizer(_:)``

指定ジェスチャ認識器に紐づくポインタをキャンセルする。

## Objective-C Declaration
```objective-c
- (void)cancelPointersForGestureRecognizer:(UIGestureRecognizer *)gestureRecognizer;
```

## Discussion
`_touchEventGestureRecognizer` の `activeTouchesByIdentifier` を走査し、引数のジェスチャ認識器が含まれるタッチに対して `_page->cancelPointer` を呼び出す。

## References
- [`WKContentViewInteraction.h#L774`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.h#L774)
- [`WKContentViewInteraction.mm#L2163`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L2163)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
