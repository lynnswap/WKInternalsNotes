# ``WKInternalsNotes/WKScrollView/_setIndicatorStyleInternal(_:)``

内部的にインジケータスタイルを設定する。

## Objective-C Declaration
```objective-c
- (void)_setIndicatorStyleInternal:(UIScrollViewIndicatorStyle)indicatorStyle;
```

## Discussion
クライアントがスタイルを設定済みであれば何もしない。未設定の場合のみ `super.indicatorStyle` を更新する。

## References
- [`WKScrollView.h#L39`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKScrollView.h#L39)
- [`WKScrollView.mm#L286`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKScrollView.mm#L286)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
