# ``WKInternalsNotes/WKWebGeolocationPolicyDecider/sharedPolicyDecider()``

共有インスタンスを返す。

## Objective-C Declaration
```objective-c
+ (instancetype)sharedPolicyDecider;
```

## Discussion
静的変数に保持しているインスタンスを返す。未生成の場合は `init` で生成してから返す。

## References
- [`WKWebGeolocationPolicyDecider.h#L40`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKWebGeolocationPolicyDecider.h#L40)
- [`WKWebGeolocationPolicyDeciderIOS.mm#L117`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKWebGeolocationPolicyDeciderIOS.mm#L117)
- [`WKWebGeolocationPolicyDeciderIOS.mm#L119`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKWebGeolocationPolicyDeciderIOS.mm#L119)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-20 |
