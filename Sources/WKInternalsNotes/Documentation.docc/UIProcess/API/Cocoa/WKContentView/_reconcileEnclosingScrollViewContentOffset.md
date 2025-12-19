# ``WKInternalsNotes/WKContentView/_reconcileEnclosingScrollViewContentOffset(_:)``

スクロールオフセットのズレを editor state に反映する。

## Objective-C Declaration
```objective-c
- (void)_reconcileEnclosingScrollViewContentOffset:(WebKit::EditorState&)state;
```

## Discussion
可視データから取得したスクロール位置と現在のスクロールビューの差分を計算し、閾値を超える場合に editor state を補正する。

## References
- [`WKContentViewInteraction.h#L815`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.h#L815)
- [`WKContentViewInteraction.mm#L8824`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L8824)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
