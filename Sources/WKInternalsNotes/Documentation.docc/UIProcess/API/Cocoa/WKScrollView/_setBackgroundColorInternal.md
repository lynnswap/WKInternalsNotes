# ``WKInternalsNotes/WKScrollView/_setBackgroundColorInternal(_:)``

内部的に背景色を設定する。

## Objective-C Declaration
```objective-c
- (void)_setBackgroundColorInternal:(UIColor *)backgroundColor;
```

## Discussion
クライアントが背景色を明示設定している場合は何もしない。そうでなければ `super.backgroundColor` を更新し、内部 delegate のキャッシュをリセットする。

## References
- [`WKScrollView.h#L38`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKScrollView.h#L38)
- [`WKScrollView.mm#L266`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKScrollView.mm#L266)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
