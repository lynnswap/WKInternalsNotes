# ``WKInternalsNotes/WKScrollView/_resetContentInset()``

`contentInset` を初期値に戻す。

## Objective-C Declaration
```objective-c
- (void)_resetContentInset;
```

## Discussion
`contentInset` を `UIEdgeInsetsZero` に戻し、可視領域の更新をスケジュールする。

## References
- [`WKScrollView.h#L47`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKScrollView.h#L47)
- [`WKScrollView.mm#L333`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKScrollView.mm#L333)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
