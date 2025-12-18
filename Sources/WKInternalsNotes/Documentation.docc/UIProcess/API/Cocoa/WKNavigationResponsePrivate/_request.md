# ``WKInternalsNotes/WKNavigationResponse/_request``

レスポンスに対応するリクエストを返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly) NSURLRequest *_request;
```

## Default Value
`_navigationResponse->request().nsURLRequest(WebCore::HTTPBodyUpdatePolicy::DoNotUpdateHTTPBody)` の結果。

## Discussion
HTTP body を更新しないポリシーで `NSURLRequest` を生成して返す。

## References
- [`WKNavigationResponsePrivate.h#L34`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKNavigationResponsePrivate.h#L34)
- [`WKNavigationResponse.mm#L94`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKNavigationResponse.mm#L94)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
