# ``WKInternalsNotes/WKProcessPool/_setObjectsForBundleParametersWithDictionary(_:)``

バンドルパラメータを辞書でまとめて設定する。

## Objective-C Declaration
```objective-c
- (void)_setObjectsForBundleParametersWithDictionary:(NSDictionary *)dictionary WK_API_AVAILABLE(macos(10.12), ios(10.0));
```

## Discussion
dictionary を copyItems で複製して secure coding でエンコードし、`setValuesForKeysWithDictionary` で反映した後 `SetInjectedBundleParameters` を送信する。

## References
- [`WKProcessPoolPrivate.h#L91`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKProcessPoolPrivate.h#L91)
- [`WKProcessPool.mm#L284`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKProcessPool.mm#L284)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
