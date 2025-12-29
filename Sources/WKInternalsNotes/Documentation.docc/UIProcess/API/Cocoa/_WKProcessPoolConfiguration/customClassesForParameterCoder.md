# ``WKInternalsNotes/_WKProcessPoolConfiguration/customClassesForParameterCoder``

パラメータコーダ用のクラスセットを返すが、現在は常に空。

## Objective-C Declaration
```objective-c
@property (nonatomic, copy) NSSet<Class> *customClassesForParameterCoder WK_API_DEPRECATED("No longer supported", macos(10.15.4, 14.0), ios(13.4, 17.0));
```

## Default Value
常に空の `NSSet` を返す。

## Discussion
getter は `NSSet` の空集合を返し、setter は何もしないため、設定しても効果はない。

## References
- [`_WKProcessPoolConfiguration.mm#L72`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKProcessPoolConfiguration.mm#L72)
- [`_WKProcessPoolConfiguration.mm#L77`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKProcessPoolConfiguration.mm#L77)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-29 |
