# ``WKInternalsNotes/WKProcessPool/_objectForBundleParameter(_:)``

指定キーのバンドルパラメータ値を返す。

## Objective-C Declaration
```objective-c
- (id)_objectForBundleParameter:(NSString *)parameter;
```

## Discussion
`protectedProcessPool(self)->protectedBundleParameters()` の辞書から `parameter` を取り出して返す。

## References
- [`WKProcessPoolPrivate.h#L88`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKProcessPoolPrivate.h#L88)
- [`WKProcessPool.mm#L257`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKProcessPool.mm#L257)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
