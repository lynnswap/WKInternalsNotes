# ``WKInternalsNotes/WKContentView/requestRectForFoundTextRange(_:completionHandler:)``

検索結果の範囲に対応する矩形を要求する。

## Objective-C Declaration
```objective-c
- (void)requestRectForFoundTextRange:(UITextRange *)range completionHandler:(void (^)(CGRect))completionHandler;
```

## Discussion
`range` が `WKFoundTextRange` のとき、`WebPageProxy` に矩形取得を依頼し、`completionHandler` に `FloatRect` を `CGRect` として渡す。`WKFoundTextRange` 以外の `UITextRange` では `CGRectZero` を返す。

## References
- [`WKContentViewInteraction.h#L990`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.h#L990)
- [`WKContentViewInteraction.mm#L12787`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L12787)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
