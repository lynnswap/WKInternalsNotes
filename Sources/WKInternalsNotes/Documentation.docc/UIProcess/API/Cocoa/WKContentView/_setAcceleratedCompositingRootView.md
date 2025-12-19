# ``WKInternalsNotes/WKContentView/_setAcceleratedCompositingRootView(_:)``

アクセラレーテッドコンポジット用のルートビューを設定する。

## Objective-C Declaration
```objective-c
- (void)_setAcceleratedCompositingRootView:(UIView *)rootView;
```

## Discussion
`_rootContentView` の子ビューを置き換え、`rootView` を追加する。

## References
- [`WKContentView.h#L122`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentView.h#L122)
- [`WKContentView.mm#L1043`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentView.mm#L1043)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
