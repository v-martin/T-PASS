### Тестовое задание T-PASS

Реализовано API по ТЗ. Также есть авторизация.

Документация openAPI (Swagger):

openapi: 3.0.3
info:
  title: T-PASS API
  version: 1.0.0
  description: API for booking media stages
paths:
  /api/bookings/:
    get:
      operationId: api_bookings_list
      description: |-
        View for managing bookings.
        - CRUD operations on bookings.
        - Supports user-specific bookings creation.
      tags:
      - api
      security:
      - tokenAuth: []
      responses:
        '200':
          content:
            application/json:
              schema:
                type: array
                items:
                  $ref: '#/components/schemas/Booking'
          description: ''
    post:
      operationId: api_bookings_create
      description: |-
        View for managing bookings.
        - CRUD operations on bookings.
        - Supports user-specific bookings creation.
      tags:
      - api
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/Booking'
          application/x-www-form-urlencoded:
            schema:
              $ref: '#/components/schemas/Booking'
          multipart/form-data:
            schema:
              $ref: '#/components/schemas/Booking'
        required: true
      security:
      - tokenAuth: []
      responses:
        '201':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Booking'
          description: ''
  /api/bookings/{id}/:
    get:
      operationId: api_bookings_retrieve
      description: |-
        View for managing bookings.
        - CRUD operations on bookings.
        - Supports user-specific bookings creation.
      parameters:
      - in: path
        name: id
        schema:
          type: string
        required: true
      tags:
      - api
      security:
      - tokenAuth: []
      responses:
        '200':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Booking'
          description: ''
    put:
      operationId: api_bookings_update
      description: |-
        View for managing bookings.
        - CRUD operations on bookings.
        - Supports user-specific bookings creation.
      parameters:
      - in: path
        name: id
        schema:
          type: string
        required: true
      tags:
      - api
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/Booking'
          application/x-www-form-urlencoded:
            schema:
              $ref: '#/components/schemas/Booking'
          multipart/form-data:
            schema:
              $ref: '#/components/schemas/Booking'
        required: true
      security:
      - tokenAuth: []
      responses:
        '200':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Booking'
          description: ''
    patch:
      operationId: api_bookings_partial_update
      description: |-
        View for managing bookings.
        - CRUD operations on bookings.
        - Supports user-specific bookings creation.
      parameters:
      - in: path
        name: id
        schema:
          type: string
        required: true
      tags:
      - api
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/PatchedBooking'
          application/x-www-form-urlencoded:
            schema:
              $ref: '#/components/schemas/PatchedBooking'
          multipart/form-data:
            schema:
              $ref: '#/components/schemas/PatchedBooking'
      security:
      - tokenAuth: []
      responses:
        '200':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Booking'
          description: ''
    delete:
      operationId: api_bookings_destroy
      description: |-
        View for managing bookings.
        - CRUD operations on bookings.
        - Supports user-specific bookings creation.
      parameters:
      - in: path
        name: id
        schema:
          type: string
        required: true
      tags:
      - api
      security:
      - tokenAuth: []
      responses:
        '204':
          description: No response body
  /api/deactivate-bookings/:
    patch:
      operationId: api_deactivate_bookings_partial_update
      description: |-
        View for deactivating all bookings.
        - Admin-only endpoint.
      tags:
      - api
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/PatchedBooking'
          application/x-www-form-urlencoded:
            schema:
              $ref: '#/components/schemas/PatchedBooking'
          multipart/form-data:
            schema:
              $ref: '#/components/schemas/PatchedBooking'
      security:
      - tokenAuth: []
      responses:
        '200':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Booking'
          description: ''
  /api/services/:
    get:
      operationId: api_services_list
      description: |-
        View for managing services.
        - CRUD operations on services.
      tags:
      - api
      security:
      - tokenAuth: []
      responses:
        '200':
          content:
            application/json:
              schema:
                type: array
                items:
                  $ref: '#/components/schemas/Service'
          description: ''
    post:
      operationId: api_services_create
      description: |-
        View for managing services.
        - CRUD operations on services.
      tags:
      - api
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/Service'
          application/x-www-form-urlencoded:
            schema:
              $ref: '#/components/schemas/Service'
          multipart/form-data:
            schema:
              $ref: '#/components/schemas/Service'
        required: true
      security:
      - tokenAuth: []
      responses:
        '201':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Service'
          description: ''
  /api/services/{id}/:
    get:
      operationId: api_services_retrieve
      description: |-
        View for managing services.
        - CRUD operations on services.
      parameters:
      - in: path
        name: id
        schema:
          type: integer
        description: A unique integer value identifying this service.
        required: true
      tags:
      - api
      security:
      - tokenAuth: []
      responses:
        '200':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Service'
          description: ''
    put:
      operationId: api_services_update
      description: |-
        View for managing services.
        - CRUD operations on services.
      parameters:
      - in: path
        name: id
        schema:
          type: integer
        description: A unique integer value identifying this service.
        required: true
      tags:
      - api
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/Service'
          application/x-www-form-urlencoded:
            schema:
              $ref: '#/components/schemas/Service'
          multipart/form-data:
            schema:
              $ref: '#/components/schemas/Service'
        required: true
      security:
      - tokenAuth: []
      responses:
        '200':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Service'
          description: ''
    patch:
      operationId: api_services_partial_update
      description: |-
        View for managing services.
        - CRUD operations on services.
      parameters:
      - in: path
        name: id
        schema:
          type: integer
        description: A unique integer value identifying this service.
        required: true
      tags:
      - api
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/PatchedService'
          application/x-www-form-urlencoded:
            schema:
              $ref: '#/components/schemas/PatchedService'
          multipart/form-data:
            schema:
              $ref: '#/components/schemas/PatchedService'
      security:
      - tokenAuth: []
      responses:
        '200':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Service'
          description: ''
    delete:
      operationId: api_services_destroy
      description: |-
        View for managing services.
        - CRUD operations on services.
      parameters:
      - in: path
        name: id
        schema:
          type: integer
        description: A unique integer value identifying this service.
        required: true
      tags:
      - api
      security:
      - tokenAuth: []
      responses:
        '204':
          description: No response body
  /api/stages/:
    get:
      operationId: api_stages_list
      description: |-
        View for managing musical stages.
        - CRUD operations on stages.
        - Supports filtering by services.
      tags:
      - api
      security:
      - tokenAuth: []
      responses:
        '200':
          content:
            application/json:
              schema:
                type: array
                items:
                  $ref: '#/components/schemas/Stage'
          description: ''
    post:
      operationId: api_stages_create
      description: |-
        View for managing musical stages.
        - CRUD operations on stages.
        - Supports filtering by services.
      tags:
      - api
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/Stage'
          application/x-www-form-urlencoded:
            schema:
              $ref: '#/components/schemas/Stage'
          multipart/form-data:
            schema:
              $ref: '#/components/schemas/Stage'
        required: true
      security:
      - tokenAuth: []
      responses:
        '201':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Stage'
          description: ''
  /api/stages/{id}/:
    get:
      operationId: api_stages_retrieve
      description: |-
        View for managing musical stages.
        - CRUD operations on stages.
        - Supports filtering by services.
      parameters:
      - in: path
        name: id
        schema:
          type: integer
        description: A unique integer value identifying this stage.
        required: true
      tags:
      - api
      security:
      - tokenAuth: []
      responses:
        '200':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Stage'
          description: ''
    put:
      operationId: api_stages_update
      description: |-
        View for managing musical stages.
        - CRUD operations on stages.
        - Supports filtering by services.
      parameters:
      - in: path
        name: id
        schema:
          type: integer
        description: A unique integer value identifying this stage.
        required: true
      tags:
      - api
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/Stage'
          application/x-www-form-urlencoded:
            schema:
              $ref: '#/components/schemas/Stage'
          multipart/form-data:
            schema:
              $ref: '#/components/schemas/Stage'
        required: true
      security:
      - tokenAuth: []
      responses:
        '200':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Stage'
          description: ''
    patch:
      operationId: api_stages_partial_update
      description: |-
        View for managing musical stages.
        - CRUD operations on stages.
        - Supports filtering by services.
      parameters:
      - in: path
        name: id
        schema:
          type: integer
        description: A unique integer value identifying this stage.
        required: true
      tags:
      - api
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/PatchedStage'
          application/x-www-form-urlencoded:
            schema:
              $ref: '#/components/schemas/PatchedStage'
          multipart/form-data:
            schema:
              $ref: '#/components/schemas/PatchedStage'
      security:
      - tokenAuth: []
      responses:
        '200':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Stage'
          description: ''
    delete:
      operationId: api_stages_destroy
      description: |-
        View for managing musical stages.
        - CRUD operations on stages.
        - Supports filtering by services.
      parameters:
      - in: path
        name: id
        schema:
          type: integer
        description: A unique integer value identifying this stage.
        required: true
      tags:
      - api
      security:
      - tokenAuth: []
      responses:
        '204':
          description: No response body
  /api/user/login/:
    post:
      operationId: api_user_login_create
      description: |-
        View for user login.
        - Extends ObtainAuthToken for token-based authentication.
        - Returns token and username on successful login.
      tags:
      - api
      requestBody:
        content:
          application/x-www-form-urlencoded:
            schema:
              $ref: '#/components/schemas/AuthToken'
          multipart/form-data:
            schema:
              $ref: '#/components/schemas/AuthToken'
          application/json:
            schema:
              $ref: '#/components/schemas/AuthToken'
        required: true
      security:
      - cookieAuth: []
      - basicAuth: []
      responses:
        '200':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/AuthToken'
          description: ''
  /api/user/logout/:
    post:
      operationId: api_user_logout_create
      description: |-
        View for user logout.
        - Requires token authentication.
        - Deletes user's authentication token.
      tags:
      - api
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/User'
          application/x-www-form-urlencoded:
            schema:
              $ref: '#/components/schemas/User'
          multipart/form-data:
            schema:
              $ref: '#/components/schemas/User'
        required: true
      security:
      - tokenAuth: []
      responses:
        '200':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/User'
          description: ''
  /api/user/signup/:
    post:
      operationId: api_user_signup_create
      description: |-
        View for user registration.
        - Allows any user to sign up.
        - Returns user details on successful registration.
      tags:
      - api
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/User'
          application/x-www-form-urlencoded:
            schema:
              $ref: '#/components/schemas/User'
          multipart/form-data:
            schema:
              $ref: '#/components/schemas/User'
        required: true
      security:
      - cookieAuth: []
      - basicAuth: []
      - {}
      responses:
        '200':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/User'
          description: ''
components:
  schemas:
    AuthToken:
      type: object
      properties:
        username:
          type: string
          writeOnly: true
        password:
          type: string
          writeOnly: true
        token:
          type: string
          readOnly: true
      required:
      - password
      - token
      - username
    Booking:
      type: object
      properties:
        id:
          type: integer
          readOnly: true
        user:
          type: integer
          readOnly: true
        start_time:
          type: string
          format: time
        finish_time:
          type: string
          format: time
        date:
          type: string
          format: date
        active:
          type: boolean
        stage:
          type: integer
      required:
      - date
      - finish_time
      - id
      - stage
      - start_time
      - user
    PatchedBooking:
      type: object
      properties:
        id:
          type: integer
          readOnly: true
        user:
          type: integer
          readOnly: true
        start_time:
          type: string
          format: time
        finish_time:
          type: string
          format: time
        date:
          type: string
          format: date
        active:
          type: boolean
        stage:
          type: integer
    PatchedService:
      type: object
      properties:
        id:
          type: integer
          readOnly: true
        name:
          type: string
          maxLength: 255
    PatchedStage:
      type: object
      properties:
        id:
          type: integer
          readOnly: true
        services:
          type: array
          items:
            type: integer
        name:
          type: string
          maxLength: 255
        address:
          type: string
          maxLength: 255
        description:
          type: string
        open_time:
          type: string
          format: time
        close_time:
          type: string
          format: time
    Service:
      type: object
      properties:
        id:
          type: integer
          readOnly: true
        name:
          type: string
          maxLength: 255
      required:
      - id
      - name
    Stage:
      type: object
      properties:
        id:
          type: integer
          readOnly: true
        services:
          type: array
          items:
            type: integer
        name:
          type: string
          maxLength: 255
        address:
          type: string
          maxLength: 255
        description:
          type: string
        open_time:
          type: string
          format: time
        close_time:
          type: string
          format: time
      required:
      - address
      - close_time
      - description
      - id
      - name
      - open_time
      - services
    User:
      type: object
      properties:
        username:
          type: string
          description: Required. 150 characters or fewer. Letters, digits and @/./+/-/_
            only.
          pattern: ^[\w.@+-]+$
          maxLength: 150
        password:
          type: string
          writeOnly: true
          maxLength: 128
        email:
          type: string
          format: email
          title: Email address
          maxLength: 254
      required:
      - password
      - username
  securitySchemes:
    basicAuth:
      type: http
      scheme: basic
    cookieAuth:
      type: apiKey
      in: cookie
      name: sessionid
    tokenAuth:
      type: apiKey
      in: header
      name: Authorization
      description: Token-based authentication with required prefix "Token"

