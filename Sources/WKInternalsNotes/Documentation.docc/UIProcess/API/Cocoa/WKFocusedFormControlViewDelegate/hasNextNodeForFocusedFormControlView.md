# ``WKInternalsNotes/WKFocusedFormControlViewDelegate/hasNextNodeForFocusedFormControlView(_:)``

次のノードが存在するかを返す。

## Objective-C Declaration
```objective-c
- (BOOL)hasNextNodeForFocusedFormControlView:(WKFocusedFormControlView *)view;
```

## Discussion
`reloadData:` が `hasNextNodeForFocusedFormControlView:` を呼び出し、`hasNextNode` に反映する。

## References
- [`WKFocusedFormControlView.h#L43`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/forms/WKFocusedFormControlView.h#L43)
- [`WKFocusedFormControlView.mm#L272`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/forms/WKFocusedFormControlView.mm#L272)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
